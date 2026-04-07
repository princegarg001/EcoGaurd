import DefaultTheme from 'vitepress/theme'
import './custom.css'

const PANEL_ID = 'data-health-panel'

function setText(id: string, value: string): void {
	const el = document.getElementById(id)
	if (el) el.textContent = value
}

function setStatus(kind: 'healthy' | 'warning' | 'error' | 'checking', text: string): void {
	const el = document.getElementById('health-status')
	if (!el) return
	el.className = `health-pill health-pill--${kind}`
	el.textContent = text
}

function parseTimestamp(raw: unknown): Date | null {
	if (!raw || typeof raw !== 'string') return null
	const value = raw.endsWith('Z') ? raw : `${raw}Z`
	const date = new Date(value)
	return Number.isNaN(date.getTime()) ? null : date
}

function formatAgeMinutes(timestamp: Date): number {
	return Math.max(0, Math.floor((Date.now() - timestamp.getTime()) / 60000))
}

async function refreshDataHealth(): Promise<void> {
	const panel = document.getElementById(PANEL_ID)
	if (!panel) return

	setStatus('checking', 'Checking')

	try {
		const [summaryResponse, dailyResponse] = await Promise.all([
			fetch('./api/summary.json', { cache: 'no-store' }),
			fetch('./api/daily-metrics.json', { cache: 'no-store' })
		])

		if (!summaryResponse.ok || !dailyResponse.ok) {
			throw new Error(`HTTP ${summaryResponse.status}/${dailyResponse.status}`)
		}

		const summary = await summaryResponse.json() as Record<string, unknown>
		const daily = await dailyResponse.json() as Array<Record<string, unknown>>

		const timestamp = parseTimestamp(summary.timestamp)
		const minutesOld = timestamp ? formatAgeMinutes(timestamp) : null

		const source = String(summary.data_source ?? 'unknown')
		const carbonSource = String(summary.carbon_intensity_source ?? 'unknown')
		const gitlabSource = String(summary.gitlab_data_source ?? 'unknown')
		const records = Array.isArray(daily) ? daily.length : 0

		if (minutesOld === null) {
			setStatus('warning', 'Unknown freshness')
			setText('health-updated-at', 'Unknown timestamp')
			setText('health-hint', 'Data loaded, but timestamp format could not be parsed.')
		} else if (minutesOld <= 90) {
			setStatus('healthy', 'Healthy')
			setText('health-updated-at', `${minutesOld} min ago`)
			setText('health-hint', 'Data pipeline looks healthy. Scheduled updates are recent.')
		} else if (minutesOld <= 1440) {
			setStatus('warning', 'Stale')
			setText('health-updated-at', `${minutesOld} min ago`)
			setText('health-hint', 'Data is available but older than expected for a frequent refresh.')
		} else {
			setStatus('error', 'Outdated')
			setText('health-updated-at', `${minutesOld} min ago`)
			setText('health-hint', 'Data appears outdated. Check scheduled workflow and API secrets.')
		}

		setText('health-source', source)
		setText('health-records', String(records))
		setText('health-carbon-source', carbonSource)
		setText('health-gitlab-source', gitlabSource)
	} catch (error) {
		console.error('EcoGuard health check failed:', error)
		setStatus('error', 'Unavailable')
		setText('health-updated-at', 'Unavailable')
		setText('health-source', 'Unavailable')
		setText('health-records', 'Unavailable')
		setText('health-carbon-source', 'Unavailable')
		setText('health-gitlab-source', 'Unavailable')
		setText('health-hint', 'Could not load api/summary.json or api/daily-metrics.json from this deployment.')
	}
}

function installHealthPoller(): void {
	if (typeof window === 'undefined') return
	const flag = '__ecoGuardHealthPollerInstalled'
	const marker = window as Window & { [key: string]: unknown }
	if (marker[flag]) return
	marker[flag] = true

	const trigger = (): void => {
		if (document.getElementById(PANEL_ID)) {
			void refreshDataHealth()
		}
	}

	trigger()
	window.setInterval(trigger, 60000)

	document.addEventListener('click', () => {
		window.setTimeout(trigger, 150)
	})

	window.addEventListener('popstate', trigger)
}

export default {
	...DefaultTheme,
	enhanceApp() {
		installHealthPoller()
	}
}

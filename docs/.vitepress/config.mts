import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'en-US',
  title: 'EcoGuard',
  description: 'Structured documentation for EcoGuard, the GitLab sustainability platform.',
  lastUpdated: true,
  cleanUrls: true,
  ignoreDeadLinks: true,
  themeConfig: {
    siteTitle: 'EcoGuard Docs',
    nav: [
      { text: 'Guide', link: '/getting-started' },
      { text: 'Architecture', link: '/architecture' },
      { text: 'Dashboard', link: '/dashboard' },
      { text: 'Live Dashboard', link: '/live-dashboard' },
      { text: 'GitLab', link: 'https://gitlab.com/princegarg001-group/EcoGuard' }
    ],
    sidebar: {
      '/': [
        {
          text: 'Overview',
          items: [
            { text: 'Home', link: '/' },
            { text: 'Getting Started', link: '/getting-started' },
            { text: 'Architecture', link: '/architecture' }
          ]
        },
        {
          text: 'Core System',
          items: [
            { text: 'Agents', link: '/agents' },
            { text: 'Flows', link: '/flows' },
            { text: 'SDLC Models', link: '/sdlc-models' },
            { text: 'Real Data Collection', link: '/real-data' }
          ]
        },
        {
          text: 'Setup & Usage',
          items: [
            { text: 'API Setup', link: '/api-setup' },
            { text: 'Dashboard', link: '/dashboard' },
            { text: 'Live Dashboard', link: '/live-dashboard' },
            { text: 'CI/CD', link: '/ci-cd' },
            { text: 'Testing', link: '/testing' }
          ]
        },
        {
          text: 'Reference',
          items: [
            { text: 'Troubleshooting', link: '/troubleshooting' },
            { text: 'Contributing', link: '/contributing' }
          ]
        }
      ]
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/princegarg001/EcoGaurd' }
    ],
    footer: {
      message: 'EcoGuard sustainability documentation',
      copyright: 'MIT License'
    },
    outline: {
      level: [2, 3]
    },
    editLink: {
      pattern: 'https://gitlab.com/princegarg001-group/EcoGuard/-/edit/main/docs/:path'
    },
    search: {
      provider: 'local'
    }
  },
  head: [
    ['meta', { name: 'theme-color', content: '#10b981' }],
    ['meta', { name: 'author', content: 'EcoGuard' }]
  ]
})

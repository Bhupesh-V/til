import { defineConfig } from 'vitepress'
import { sidebar } from './sidebar.js'
// https://vitepress.dev/reference/site-config
export default defineConfig({
  // base: '/til/',
  title: "Today I Learned",
  description: "Personal Wiki of Interesting things I learn every day at the intersection of software, life & stuff a.k.a my second brain 🧠️",
  sitemap: {
    hostname: 'https://til.bhupesh.me'
  },
  head: [
    ['link', { rel: "icon", type: "image/png", sizes: "32x32", href: "/favicon.png" }],
    ['script', { src: 'https://www.googletagmanager.com/gtag/js?id=G-7M5P7006XV' }],
    ['script', {}, ` window.dataLayer = window.dataLayer || [];\nfunction gtag(){dataLayer.push(arguments);}\ngtag('js', new Date());\ngtag('config', 'G-7M5P7006XV');`]
  ],
  themeConfig: {
    logo: '/favicon.png',
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      // { text: 'Home', link: '/' },
      { text: 'Work with me!', link: 'https://bhupesh.me/hire' },
      { text: 'Blog', link: 'https://bhupesh.me' },
      { text: 'Bookshelf', link: 'https://bookshelf.bhupesh.me/' },
    ],

    sidebar: sidebar,

    socialLinks: [
      { icon: 'github', link: 'https://github.com/bhupesh-v' },
      { icon: 'x', link: 'https://x.com/bhupeshimself' },
    ],

    footer: {
      message: 'Written while 🙇🏽‍♀️',
    },

    search: {
      provider: 'local'
    },
  },
  cleanUrls: true,
})

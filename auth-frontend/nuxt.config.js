export default {
  mode: 'universal',
  axios: {
    baseURL: 'http://backend:5000',
    browserBaseURL: 'http://localhost:5000',
  },
  head: {
    titleTemplate: '%s - ' + process.env.npm_package_name,
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || '',
      },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },
  toast: {
    duration: 3000,
  },
  loading: { color: '#fff' },
  css: [],
  plugins: [
    '@/plugins/vuetify',
    '@/plugins/axios'
  ],
  buildModules: ['@nuxtjs/eslint-module', '@nuxtjs/vuetify'],
  modules: [
    '@nuxtjs/toast',
    '@nuxtjs/axios',
    'cookie-universal-nuxt'
  ],
  build: {
    transpile: ['vuetify/lib'],
  },
}

// Each time a route is about to be rendered,
// Nuxt will check if the cookies exist and set them in the store.
// After that, a request will be made to grab uer data from server

import cookie from 'cookie'

export const actions = {
  async nuxtServerInit({ commit, dispatch }, context) {
    const cookies = cookie.parse(context.req.headers.cookie || '')
    if (cookies.accessToken) {
      await dispatch('auth/SET_TOKENS', {
        accessToken: cookies.accessToken,
        refreshToken: cookies.refreshToken,
      })

      // await this.$axios.get('/user/me').then((res) => {
      //   commit('auth/SET_USER', res.data.user)
      // })
    }
  },
}

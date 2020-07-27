import cookie from 'cookie'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const state = () => ({
  currentArticle: null
})

export const mutations = {
  SET_CURRENT_ARTICLE(state, article) {
    state.currentArticle = article
  }
}

export const actions = {
  async nuxtServerInit({ commit, dispatch }, context) {
    const cookies = cookie.parse(context.req.headers.cookie || '')
    if (cookies.accessToken) {
      await dispatch('auth/SET_TOKENS', {
        accessToken: cookies.accessToken,
        refreshToken: cookies.refreshToken
      })

      // TODO: how exactly routing of requests is going to be done depends
      // TODO: on kubernetes config which I won't decide now
      // TODO: hardcoded address as temporary solution
      await this.$axios
        .get('http://localhost:5000/api/v1/user/me')
        .then((res) => {
          commit('auth/SET_USER', res.data.user)
        })
    }
  }
}

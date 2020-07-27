export const state = () => ({
  user: null,
  accessToken: null,
  refreshToken: null,
})

export const mutations = {
  SET_ACCESS_TOKEN(state, accessToken) {
    state.accessToken = accessToken
  },
  SET_REFRESH_TOKEN(state, refreshToken) {
    state.refreshToken = refreshToken
  },
  SET_USER(state, user) {
    state.user = user
  },
}

export const getters = {
  user: (state) => state.user,
  token: (state) => state.accessToken,
}

export const actions = {
  SET_TOKENS({ commit, dispatch }, payload) {
    commit('SET_ACCESS_TOKEN', payload.accessToken)
    commit('SET_REFRESH_TOKEN', payload.refreshToken)
  },
  FETCH_USER({ commit }) {
    this.$axios.get('/user/me').then((res) => {
      commit('SET_USER', res.data.user)
    })
  },
  async LOGOUT({ commit }) {
    commit('SET_USER', null)

    Cookie.delete('accessToken')
    Cookie.delete('accessToken')

    return Promise.resolve()
  },
}

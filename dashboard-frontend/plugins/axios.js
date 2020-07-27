export default function ({ $axios, store, app }) {
  $axios.onRequest((config) => {
    if (store.state.auth.accessToken !== null) {
      config.headers.common.Authorization = `Bearer ${store.state.auth.accessToken}`
    }
  })

  $axios.onResponseError((err) => {
    const code = parseInt(err.response && err.response.status)
    const originalRequest = err.config

    if (code === 412) {
      originalRequest.__isRetryRequest = true

      const token = app.$cookies.get('refreshToken')

      $axios
        .post('user/auth/refresh', { refreshToken: token })
        .then((response) => {
          if (response.status === 200) {
            originalRequest.headers.Authorization = `Bearer ${response.data.accessToken}`
          }

          // accessToken = response.data.accessToken
          // refreshToken = response.data.refreshToken
        })
        .then((res) => {
          return $axios(originalRequest)
        })
        .catch((e) => {
          // eslint-disable-next-line
          console.log(e)
        })
    }
  })
}

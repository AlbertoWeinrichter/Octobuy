export default function ({ $axios, store, app }) {
  // maybe check expiry date on client and grab token BEFORE sending a request
  // so you cans et tokens no prob

  $axios.onRequest((config) => {
    if (store.state.auth.accessToken !== null) {
      config.headers.common[
        'Authorization'
      ] = `Bearer ${store.state.auth.accessToken}`
    }
  })

  $axios.onResponseError((err) => {
    const code = parseInt(err.response && err.response.status)

    let originalRequest = err.config
    if (code == 412) {
      originalRequest.__isRetryRequest = true

      let token = app.$cookies.get('refreshToken')
      let accessToken = null
      let refreshToken = null

      let req = $axios
          .post('user/auth/refresh', { refreshToken: token })
          .then((response) => {
            if (response.status == 200) {
              originalRequest.headers[
                'Authorization'
              ] = `Bearer ${response.data.accessToken}`
            }

            accessToken = response.data.accessToken
            refreshToken = response.data.refreshToken

          })
                .then((res) => {
          return $axios(originalRequest)
        })
        // .finally(() => {
        //   app.$cookies.set('accessToken', accessToken)
        //   app.$cookies.set('refreshToken', refreshToken)
        // })
          .catch((e) => {
            console.log(e)
          })

    }
  })
}

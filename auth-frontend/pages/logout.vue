<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-3">
              <v-card-text>
                <div class="layout column align-center">
                  <h1 class="flex my-4 primary--text">Session closed</h1>
                  <h4 class="flex my-4 primary--text">see you soon!</h4>
                </div>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
const Cookie = process.client ? require('js-cookie') : undefined

export default {
  data: () => ({
    loading: false,
    login_form: {
      email: '',
      password: '',
    },
  }),
  methods: {
    async login() {
      let response = await this.$axios.$post('/user/auth/login', this.login_form)

      this.$store.commit('SET_USER', response.user)
      Cookie.set('accessToken', response.accessToken)
      this.$axios.setHeader('Authorisation', response.accessToken)

      this.$router.push('/')
    },
  },
}
</script>
<style scoped lang="css">
#login {
  height: 50%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
  z-index: 0;
}
</style>

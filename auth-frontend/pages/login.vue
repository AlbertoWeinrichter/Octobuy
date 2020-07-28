<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-3">
              <v-card-text>
                <div class="layout column align-center">
                  <img
                    src="../static/logo.png"
                    alt="Voynich Logo"
                    width="120"
                    height="120"
                  />
                  <h1 class="flex my-4 primary--text">Octobuy</h1>
                </div>
                <v-form>
                  <v-text-field
                    name="email"
                    label="Login"
                    type="text"
                    v-model="login_form.email"
                  ></v-text-field>
                  <v-text-field
                    name="password"
                    label="Password"
                    id="password"
                    type="password"
                    v-model="login_form.password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-btn block color="primary" @click="login" :loading="loading">
                  Login
                </v-btn>

                <v-spacer></v-spacer>

              </v-card-actions>

              <br>
              <br>
              <nuxt-link to="/register">
                <i>Don't have an account?</i>
              </nuxt-link>
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
        password: ''
      }
    }),
    methods: {
      async login() {
        await this.$axios
          .$post('/user/auth/login', this.login_form)
          .then((response) => {
            Cookie.set('accessToken', response.accessToken)
            Cookie.set('refreshToken', response.refreshToken)

            this.$store.dispatch('auth/SET_TOKENS', {
              accessToken: response.accessToken,
              refreshToken: response.refreshToken
            })

            this.$store.dispatch('auth/FETCH_USER')

            this.$router.push('/')
          })
          .catch((err) => {
            console.log(err)
            this.$toast.error('User does not exist.')
          })
      }
    }
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

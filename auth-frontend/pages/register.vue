<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-3">
              <v-card-title>
                <div class="layout column align-center">
                  <h1 class="flex my-4 primary--text">REGISTER</h1>
                </div>
              </v-card-title>

              <v-card-text>
                <v-form ref="form" v-model="valid" lazy-validation>
                  <v-text-field
                    v-model="username"
                    :rules="usernameRules"
                    label="Username"
                    required
                  ></v-text-field>

                  <v-text-field
                    v-model="email"
                    :rules="emailRules"
                    label="E-mail"
                    required
                  ></v-text-field>

                  <v-text-field
                    v-model="password"
                    :append-icon="show ? 'visibility' : 'visibility_off'"
                    :rules="[passwordRules.required, passwordRules.min]"
                    :type="show ? 'text' : 'password'"
                    required
                    name="password"
                    label="Enter Password"
                    hint="At least 8 characters"
                    @click:append="show = !show"
                  ></v-text-field>

                  <v-text-field
                    v-model="confirmPassword"
                    :append-icon="show1 ? 'visibility' : 'visibility_off'"
                    :rules="[
                      passwordRules.required,
                      passwordRules.min,
                      passwordConfirmationRule,
                    ]"
                    required
                    :type="show1 ? 'text' : 'password'"
                    name="input-10-1"
                    label="Re-enter Password"
                    hint="At least 8 characters"
                    @click:append="show1 = !show1"
                  ></v-text-field>

                  <v-checkbox
                    v-model="checkbox"
                    :rules="[
                      (v) => !!v || 'You need to accept our terms & conditions',
                    ]"
                    label="Do you accept our terms & conditions?"
                    required
                  ></v-checkbox>
                </v-form>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  block
                  :disabled="!valid"
                  color="primary"
                  @click="submit"
                  :loading="loading"
                >
                  Register
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    loading: false,
    checkbox: false,
    valid: false,

    username: '',
    usernameRules: [
      (v) => !!v || 'Username is required',
      (v) => (v && v.length <= 25) || 'Username too long',
    ],
    email: '',
    emailRules: [
      (v) => !!v || 'E-mail is required',
      (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
    password: '',
    confirmPassword: '',
    show: false,
    show1: false,
    passwordRules: {
      required: (v) => !!v || 'Password is required',
      min: (v) => v.length >= 8 || 'Min 8 characters',
    },
  }),
  computed: {
    passwordConfirmationRule() {
      return this.password === this.confirmPassword || 'Password must match'
    },
  },
  methods: {
    async submit() {
      try {
        let data = {
          "username": this.username,
          "email": this.email,
          "password": this.password,
        }
        let response = await this.$axios.post('/user/auth/register', data)
        if (response.status === 202) {
          this.$toast.error('User already exists. Try to login');
        } else {
          this.$router.push('/')
        }
      } catch (err) {
        this.$toast.error('Error creating user. Please try again')
      }
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

<template>
  <v-app-bar absolute>
    <v-toolbar-title>Momentum Financial</v-toolbar-title>

    <v-spacer></v-spacer>

    <div>wii</div>

    <v-spacer></v-spacer>

    <v-btn icon>
      <v-icon>mdi-search</v-icon>
    </v-btn>

    <v-btn v-if="user" icon>
      <v-icon>mdi-account</v-icon>
    </v-btn>

    <div v-else>
      Login
    </div>
  </v-app-bar>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Header',
  data() {
    return {
      menu_items: [
        {
          title: ' Cuenta',
          icon: 'mdi-account'
        },
        {
          title: ' Logout',
          icon: 'mdi-close'
        }
      ]
    }
  },
  computed: {
    ...mapGetters('auth', ['user'])
  }
}
</script>

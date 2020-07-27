<template>
  <v-app-bar absolute>
    <v-toolbar-title>Momentum Control Panel</v-toolbar-title>

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
    }
  },
  computed: {
    ...mapGetters('auth', ['user'])
  }
}
</script>

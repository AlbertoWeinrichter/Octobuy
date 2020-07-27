<template>
  <div>
    <br />

    User: {{ user }}

    <br />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  middleware: 'auth',
  computed: {
    ...mapGetters('auth', ['user']),
  },
}
</script>

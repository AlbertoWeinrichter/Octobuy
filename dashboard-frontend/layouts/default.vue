<template>
  <div>
    <Header />

    <nuxt keep-alive />

    <the-footer />
  </div>
</template>

<script>
import Header from '@/components/Header'
import TheFooter from '@/components/TheFooter'

export default {
  components: {
    Header,
    TheFooter
  }
}
</script>

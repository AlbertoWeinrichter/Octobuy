<template>
  <v-card
    class="mx-auto"
    max-width="1200"
  >
    <v-img
      class="white--text align-end"
      height="500px"
      src="https://c.static-nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/skwgyqrbfzhu6uyeh0gg/air-max-270-shoe-8HhX8Z.jpg"
    >
      <v-card-title>Super sneaker 1</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">Number 10</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>This is an amazing pair of sneakers!</div>

      Status: {{status}}
      <div v-if="loading">
        <v-progress-circular
          indeterminate
          color="green"
        ></v-progress-circular>
      </div>

      <div v-if="error">
        Error: {{error}}
      </div>

    </v-card-text>

    <v-card-actions>
      <v-btn
        color="orange"
        text
      >
        Cancel Order
      </v-btn>

      <v-btn
        color="orange"
        text
        @click="buy_process"
      >
        Start buy process
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  export default {
    middleware: 'auth',
    name: "productPage",
    data: () => ({
      items: [
        {
          id: 1,
          color: '#1F7087',
          src: 'https://c.static-nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/skwgyqrbfzhu6uyeh0gg/air-max-270-shoe-8HhX8Z.jpg',
          title: 'Super sneaker 1',
          description: 'This is an amazing pair of sneakers!',
        },
      ],
      status: "Not Started",
      error: null,
      loading: false
    }),
    methods: {
      async buy_process() {
        this.status = "Buying";
        this.loading = true
        await this.$axios
          .$get('/user/bot/1')
          .then((response) => {
            console.log(response)
          })
          .catch((err) => {
            this.loading = false
            this.status = err
            console.log(err)
            this.$toast.error('Bot failed for some reason')
          })
      }
    }
  }
</script>

<style scoped>

</style>

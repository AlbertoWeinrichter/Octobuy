<template>
  <v-card
    max-width="2000"
    class="mx-auto"
  >

    <v-container>
      <v-row dense>
        <v-col
          v-for="(item, i) in items"
          :key="i"
          cols="12"
        >
          <v-card
            :color="item.color"
            dark
          >
            <div class="d-flex flex-no-wrap justify-space-between">
              <div>
                <v-card-title
                  class="headline"
                  v-text="item.title"
                ></v-card-title>

                <v-card-subtitle v-text="item.description"></v-card-subtitle>
              </div>

              <v-avatar
                class="ma-3"
                size="125"
                tile
              >
                <v-img :src="item.src"></v-img>
              </v-avatar>

              <v-card-actions>
                <nuxt-link
                  :to="'orders/' + item.id"
                  tag="product"
                >
                  Order Details
                </nuxt-link>
              </v-card-actions>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
  export default {
    name: "orders",
    middleware: 'auth',
    data: () => ({
      items: [
        {
          id: 1,
          color: '#1F7087',
          src: 'https://c.static-nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/skwgyqrbfzhu6uyeh0gg/air-max-270-shoe-8HhX8Z.jpg',
          title: 'Super sneaker 1',
          description: 'This is an amazing pair of sneakers!',
        },
        {
          id: 2,
          color: '#952175',
          src: 'https://c.static-nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/r6jpmsemr7rmvuq7qh7e/air-tailwind-79-shoe-ScqzZG.jpg',
          title: 'Super sneaker 2',
          description: 'This is an amazing pair of sneakers!',
        },
        {
          id: 3,
          color: '#385F73',
          src: 'https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/de317847-20e7-48a5-93a9-36295235e4cf/court-vintage-shoe-17xdGn.jpg',
          title: 'Super sneaker 3',
          description: 'This is an amazing pair of sneakers!',
        },
      ],
    })
  }
</script>

<style scoped>

</style>

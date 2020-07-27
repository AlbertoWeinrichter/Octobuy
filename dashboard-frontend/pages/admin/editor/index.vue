<template>
  <section class="container">
    <v-row align="center">
      <v-expansion-panels inset hover tile>
        <nuxt-link to="/admin/editor/new">
          <v-btn absolute dark fab top right color="green">
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </nuxt-link>
        <v-expansion-panel
          v-for="(publication, index) in publication_list"
          :key="index"
        >
          <v-expansion-panel-header>
            <h5>{{ publication.title }}</h5>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-card>
              <v-list-item three-line>
                <v-list-item-avatar
                  tile
                  size="80"
                  color="grey"
                ></v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-subtitle>
                    {{ publication.description }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>

              <v-card-actions>
                <v-btn color="green">Edit</v-btn>
                <v-btn color="red">Delete</v-btn>
              </v-card-actions>
            </v-card>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>
  </section>
</template>

<script>
export default {
  layout: 'admin',
  name: 'Editor',
  async fetch() {
    await this.$axios
      .get('/publication')
      .then((response) => {
        this.publication_list = response.data.publication_list
        this.$router.push('/')
      })
      .catch((err) => {
        // eslint-disable-next-line
        console.log(err.message)
        this.$toast.error('Error loading publications.')
      })
  },
  data() {
    return {
      publication_list: {}
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  /*width: 60%;*/
  /*margin: 0 auto;*/
  padding: 50px 0;
}
</style>

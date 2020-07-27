<template>
  <section class="container">
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-btn right dark color="green" @click="submit">
        Save
      </v-btn>

      <v-row>
        <v-flex xs11 sm11 md5 lg5 xl5>
          <v-dialog ref="dialog" width="290px">
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="form.publicationDate"
                label="Publication Date"
                readonly
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker v-model="form.publicationDate" scrollable>
              <v-spacer></v-spacer>
              <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
              <v-btn flat color="primary" @click="$refs.dialog.save(date)"
                >OK
              </v-btn>
            </v-date-picker>
          </v-dialog>
        </v-flex>
        <v-flex xs11 sm11 offset-md-2 md5 offset-lg-2 lg5 offset-xl-2 xl5>
          <v-file-input
            v-model="form.socialImage"
            accept="image/*"
            label="Social image"
            @change="imageUpload"
          ></v-file-input>
        </v-flex>
      </v-row>

      <v-row>
        <v-flex xs11 sm11 md5 lg5 xl5>
          <v-select
            v-model="form.typeOf"
            :items="['Premium', 'Normal']"
            label="Type"
          ></v-select>
        </v-flex>

        <v-flex xs11 sm11 offset-md-2 md5 offset-lg-2 lg5 offset-xl-2 xl5>
          <v-file-input
            v-model="form.coverImage"
            accept="image/*"
            label="Cover image"
            @change="imageUpload"
          ></v-file-input>
        </v-flex>
      </v-row>

      <v-row>
        <v-flex>
          <v-text-field
            v-model="form.title"
            :rules="form.titleRules"
            label="Title"
            required
          ></v-text-field>
        </v-flex>
      </v-row>

      <v-row>
        <v-flex>
          <v-text-field
            v-model="form.slug"
            :rules="form.slugRules"
            label="Slug"
            required
          ></v-text-field>
        </v-flex>
      </v-row>

      <v-row>
        <v-flex>
          <v-text-field
            v-model="form.description"
            :rules="form.descriptionRules"
            label="Description"
          ></v-text-field>
        </v-flex>
      </v-row>
    </v-form>
    <client-only>
      <vue-editor id="editor" v-model="form.body_html"> </vue-editor>
      <!--TODO: dont forget to use me in s3-->
      <!--useCustomImageHandler-->
      <!--@imageAdded="handleImageAdded"-->
    </client-only>
  </section>
</template>

<script>
export default {
  layout: 'admin',
  name: 'Editor',
  data() {
    return {
      valid: false,
      editorOption: {
        theme: 'snow',
        modules: {
          toolbar: [
            ['bold', 'italic', 'underline', 'strike'],
            ['blockquote', 'code-block']
          ]
        }
      },
      form: {
        tags: [],
        summary: [],
        body_html: '<p>I am Example</p>',
        typeOf: null,
        publicationDate: null,
        publicationDateRules: [
          //  should check its not before today
        ],
        title: '',
        titleRules: [
          (v) => !!v || 'A title is required',
          (v) => (v && v.length <= 200) || 'Title too long',
          (v) => (v && v.length >= 5) || 'Title too short'
        ],
        slug: '',
        slugRules: [
          (v) => !!v || 'A slug is required',
          (v) => (v && v.length <= 50) || 'Slug too long',
          (v) => (v && v.length >= 5) || 'Slug too short'
        ],
        description: '',
        descriptionRules: [(v) => !!v || 'The description is empty'],
        coverImage: null,
        socialImage: null
      }
    }
  },
  methods: {
    checkIfNew() {
      if (this.$route.fullPath === 'new') {
        this.form.title = 'New publication'
      } else {
        this.loadPubFromDb()
      }
    },
    handleImageAdded(file, Editor, cursorLocation, resetUploader) {
      const formData = new FormData()
      formData.append('image', file)

      this.$axios({
        url: 'https://fakeapi.yoursite.com/images',
        method: 'POST',
        data: formData
      })
        .then((result) => {
          Editor.insertEmbed(cursorLocation, 'image', result.data.url)
          resetUploader()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    imageUpload(e) {
      alert(1)
    },
    async submit() {
      try {
        const data = {
          title: this.form.title,
          typeOf: this.form.typeOf,
          slug: this.form.slug,
          publicationDate: this.form.publicationDate,
          description: this.form.description,
          coverImage: this.form.coverImage,
          socialImage: this.form.socialImage,
          bodyHtml: this.form.body_html,
          tags: this.form.tags,
          summary: this.form.summary
        }
        console.log(data)
        const response = await this.$axios.post('/publication', data)
        if (response.status === 202) {
          this.$toast.error('Title. Try to login', { duration: 500 })
        } else {
          this.$router.push('/admin/editor')
          this.$toast.success('Publication created!', { duration: 500 })
        }
      } catch (err) {
        // eslint-disable-next-line
        console.log(err)
        this.$toast.error('Error creating publication. Please try again', {
          duration: 500
        })
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  width: 100%;
  margin: 0 auto;
  padding: 50px 0;
  .quill-editor {
    min-height: 200px;
    max-height: 400px;
    overflow-y: auto;
  }
}
</style>

<script>
export default {
  props: {
    markdown: {
      type: Object,
      required: true
    }
  },
  created() {
    this.templateRender = new Function(this.markdown.vue.render)()
    this.$options.staticRenderFns = new Function(
      this.markdown.vue.staticRenderFns
    )()
  },
  render(h) {
    return this.templateRender ? this.templateRender() : h('div')
  }
}
</script>

<style>
.markdown {
  /* Put your Markdown styles here */
}
</style>


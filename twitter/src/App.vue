<template>
  <v-app>
    <v-main>
      <Twitter/>
    </v-main>
  </v-app>
</template>

<script>
import Twitter from './components/layouts/twitter/index.vue'

export default {
  name: 'App',

  components: {
    Twitter,
  },

  data: () => ({
    //
  }),
}
</script>

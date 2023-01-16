<script>
import { store } from '../src/store';
import IntscoreHeader from '../src/components/IntscoreHeader.vue'

export default {
  name: "App",
  components: {
    IntscoreHeader,
  },
  data() {
    return {
      store,
    }
  },
  methods: {
  },
  mounted(){

  }
}  
</script>

<template>
<IntscoreHeader></IntscoreHeader>
</template>

<style lang="scss">
@use './style/variables.scss' as *;
</style>
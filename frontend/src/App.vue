<script>
import { store } from '../src/store';
import IntscoreHeader from '../src/components/IntscoreHeader.vue'
import IntscoreMain from '../src/components/IntscoreMain.vue'

export default {
  name: "App",
  components: {
    IntscoreHeader,
    IntscoreMain,
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
<IntscoreMain></IntscoreMain>
</template>

<style lang="scss">
@use './style/variables.scss' as *;
</style>
<script>
import MainCard from './MainCard.vue';
import { store } from '../../store';

export default {
  name: "MainLedger",
  components: {
    MainCard
  },
  data() {
    return {
      store,
    }
  }
}
</script>

<template>
  <div class="contenitore">
    <div v-for="(card, index) in store.Source" :key="index">
      <MainCard
        :paese="card.tag"
        :punteggio="card.score"
      ></MainCard>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use '../../style/variables.scss' as *;

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
}
.contenitore {
  display: flex;
  justify-content: flex-start;
  padding: 20px;
  gap: 5px;
  flex-direction: column;
  
}
</style>
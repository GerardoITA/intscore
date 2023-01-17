<script>
import MainCard from './MainCard.vue';
import { store } from '../../store';
import axios from 'axios';

export default {
  name: "MainLedger",
  components: {
    MainCard
  },
  data() {
    return {
      store,
      
    }
  },
  methods: {
      getJson() {
        let countryapi = store.source;
        axios
          .get(countryapi)
          .then(res => {
            store.countries = res.data;
            console.log(store.countries);
          });
      },
  },
  mounted(){
    this.getJson();
  }
}
</script>

<template>
  <div class="contenitore">
    <div v-for="(card, index) in store.countries[store.selectedJson]" :key="index">
      <MainCard
        :paese="card.tag"
        :punteggio="card.score"
      ></MainCard>
    </div>
    <div :class='store.pickedSave ? "hidden" : ""'>
     Please select a save.
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
.hidden {
  display: none;
}
</style>
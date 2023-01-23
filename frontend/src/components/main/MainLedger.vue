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
          });
      },
  },
  mounted(){
    this.getJson();
  },
  computed: {
    sortedItems() {
      if (store.countries[store.selectedJson]) {
        return store.countries[store.selectedJson].sort((a, b) => {
          return parseInt(b.score) - parseInt(a.score);
        });
      };
    }
  }
}
</script>

<template>
  <div class="contenitore">
    <div v-for="(card, index) in sortedItems" :key="index">
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
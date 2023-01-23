<script>
import { store } from '../../store';
import axios from 'axios';

export default {
  name: "MainMenu",
  data() {
    return {
      store,
    }
  },
  methods: {
    getPathJson() {
      let pathJson = store.jsonFolder;
      axios
        .get(pathJson)
        .then(res => {
          store.jsonList = res.data;
        });
    },
    isSavePicked() {
      if (store.selectedJson !== ".json") {
        store.pickedSave = true;
      }
    }
  },
  mounted() {
    this.getPathJson(),
    this.isSavePicked()
  }
}
</script>

<template>
  <div class="menu">
    <select v-model="store.selectedJson" @change="isSavePicked">
      <option v-for="file in store.jsonList" :key="file" :value="file">
        {{ file }}
      </option>
    </select>
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
.menu {
  display: flex;
}
select {
  background-color: white;
  color: $MineShaft;
  border: 3px solid $MineShaft;
  padding: 5px;
  border-radius: 8px;
  margin: 20px auto;
  width: 80%;
    
}
</style>
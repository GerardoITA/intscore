<script>
import { store } from '../../store';
export default {
  name: "",
  data() {
    return {
      store,
    }
  }
}
</script>

<template>
  <div class="nazione">
    <div class="nazione_tag">
      aaa
    </div>
    <div class="nazione_score">
      22.000
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
  .nazione {
    display: flex;
    
    border: 3px solid $MineShaft;
    border-radius: 8px;
    .nazione_tag {
      padding: 5px;
      width: 80%;
      border-right: 3px solid $MineShaft;
    }
    .nazione_score {
      padding: 5px;
      display: flex;
     
    }
  }
}
</style>
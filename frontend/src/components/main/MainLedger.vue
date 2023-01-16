<script>
export default {
  name: "",
  data() {
    return {

    }
  }
}
</script>

<template>
  <div class="contenitore">
    <div class="nazione">
      <div class="nazione_tag">
        aaa
      </div>
      <div class="nazione_score">
      
      </div>
    </div>
    <div class="nazione">
      aaa
    </div>
    <div class="nazione">
      aaa
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
    padding: 5px;
    border: 3px solid $MineShaft;
    border-radius: 8px;
    .nazione_tag {
      width: 80%;
      border-right: 3px solid $MineShaft;
    }
  }
}
</style>
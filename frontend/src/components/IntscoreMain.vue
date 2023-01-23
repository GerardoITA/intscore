<script>
import MainLedger from './main/MainLedger.vue'; 
import MainMenu from './main/MainMenu.vue';
export default {
  name: "IntscoreMain",
  components: {
    MainLedger,
    MainMenu,
  },
  data() {
    return {

    }
  }
}
</script>

<template>
  <main>
    <MainLedger class="side left">
  
    </MainLedger>
    <div class="side left">
      <MainMenu>
      </MainMenu>
    </div>
  </main>
</template>

<style lang="scss" scoped>
@use '../style/variables.scss' as *;

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
}
main {
  padding: 30px 0;
  margin: 50px auto;
  width: 1200px;
  height: 900px;
  border: 5px solid $MineShaft;
  border-radius: 20px;
  display: flex;
  justify-content: space-evenly;
  .side {
    width: 550px;
    border-radius: 20px;
  }
  .left {
    border: 5px solid $MineShaft;
  }
}
h1 {
  color: $MineShaft;
}
</style>

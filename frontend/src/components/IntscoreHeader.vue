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
  <header>
    <h1>IntScore Ledger</h1>
  </header>
</template>

<style lang="scss" scoped>
@use '../style/variables.scss' as *;

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
}
header {
  padding-top: 25px;
  display: flex;
  justify-content: center;
}
h1 {
  color: $MineShaft;
}
</style>

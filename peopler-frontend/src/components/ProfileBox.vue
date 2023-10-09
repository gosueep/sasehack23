<template>
  <div class='ot'>
    <slot name='header'></slot>
    <hr/>
    <slot></slot>
  </div>
</template>

<style scoped>
  h1 {
    font-weight: 600;
    font-size: 28px;
  }
  div.ot {
    border-radius: 8px;
    box-sizing: border-box;
    border: 1px solid #ffc587;
    background: #ffffff2f;
    width: 400px;
    padding: 12px 20px;
  }
  hr {
    border: 1px solid #000;
    border-top: none;
  }
</style>

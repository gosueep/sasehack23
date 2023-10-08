<template>
  <nav>
    <router-link to="/">Landing</router-link> |
    <router-link to="/onboarding">Onboarding</router-link> |
    <router-link to="/matching">Matching</router-link> |
    <router-link to="/connect">Connect</router-link>
  </nav>
  <div v-if='this.$route.name === "home"'>
    <router-view/>
  </div>
  <div v-else id='outer-shell'>
    <div id='outer-bg'></div>
    <div id='inner-shell'>
      <router-view/>
    </div>
  </div>
</template>

<style>
#outer-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  background: linear-gradient(120deg, #fffbd0, #ffc183)
}
#inner-shell {
  margin: auto;
  max-width: max(80vw, 800px);
  background-color: #ffffff5f;
  padding: 12px 16px;
  border-radius: 8px;
}
</style>

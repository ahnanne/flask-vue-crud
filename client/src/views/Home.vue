<template>
  <div class="home container mx-auto flex flex-col justify-center items-center">
    <div>
      <img alt="Vue logo" src="../assets/logo.png" />
    </div>
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomePage",
  components: {
    HelloWorld,
  },
};
</script>

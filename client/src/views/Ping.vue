<template>
  <div class="ping">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'Ping',
  data() {
    return {
      msg: "Pong!",
    };
  }
};
</script>
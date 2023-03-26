<template>
  <div class="ping">
    <h1 class="text-3xl font-bold underline">{{ msg }}</h1>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PingPage",

  data() {
    return {
      msg: "",
    };
  },

  methods: {
    getMessage() {
      const path = "http://localhost:5000/ping";

      axios
        .get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },

  // 컴포넌트가 생성되는 시점
  // (아직 virtual DOM 반영 X)
  created() {
    console.log("hello");
    this.getMessage();
  },
};
</script>

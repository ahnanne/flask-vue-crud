<template>
  <div class="ping">
    <h1 class="text-3xl font-bold underline">{{ msg }}</h1>

    <div class="container mx-auto py-10">
      <div
        class="border m-6 rounded-lg bg-white mx-auto max-w-sm shadow-lg rounded-lg overflow-hidden"
      >
        <div class="sm:flex sm:items-center px-6 py-4">
          <img
            class="block h-16 sm:h-24 rounded-full mx-auto mb-4 sm:mb-0 sm:mr-4 sm:ml-0"
            src="https://i.namu.wiki/i/pPviRBLcPoUmBvyWD6mgjL6m-oKYUQ27glaVyenxCQGCXzUhV37veO_ee1wMUic0Bao5whldXzzO1WQwu9CyaXUll5Ukf0gL7eNKzK5HEWt8XlMV_A8mjqDqGNc53eMX4z6UrN1XdMikxmzvo1OJMA.webp"
            alt=""
          />
          <div class="text-center sm:text-left sm:flex-grow">
            <div class="mb-4">
              <p class="text-xl leading-tight">Jane Doe</p>
              <p class="text-sm leading-tight text-grey-dark">
                Software Developer at SpongeBob LLC.
              </p>
            </div>
            <div class="flex flex-wrap">
              <button
                class="text-xs font-semibold rounded-full px-4 py-1 mx-3 leading-normal bg-white border border-blue text-blue hover:bg-blue hover:text-white"
              >
                Call
              </button>
              <button
                class="text-xs font-semibold rounded-full px-4 py-1 leading-normal bg-white border border-purple text-purple hover:bg-purple hover:text-white"
              >
                Message
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
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
      const path = `http://localhost:5000/ping/${
        this.$route.query.name || "guest"
      }`;

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

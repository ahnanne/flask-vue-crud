<template>
  <div class="container mx-auto books-container">
    <div class="flex flex-col justify-start">
      <h1 class="text-3xl font-bold">Books</h1>
      <hr />
      <br /><br />
      <button type="button" class="w-24 bg-teal-700">Add Book</button>
      <br /><br />
      <table class="border-collapse border-spacing-2 border border-slate-400">
        <thead>
          <tr>
            <th class="border border-slate-300">Title</th>
            <th class="border border-slate-300">Author</th>
            <th class="border border-slate-300">Read?</th>
            <th class="border border-slate-300"></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="border border-slate-300">foo</td>
            <td class="border border-slate-300">bar</td>
            <td class="border border-slate-300">foobar</td>
            <td class="border border-slate-300">
              <div class="btn-group" role="group">
                <button type="button" class="w-24 bg-stone-700 mr-2">Update</button>
                <button type="button" class="w-24 bg-rose-800">Delete</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "BooksPage",

  data() {
    return {
      msg: "",
    };
  },

  methods: {
    getMessage() {
      // TODO:
    },
  },

  // 컴포넌트가 생성되는 시점
  // (아직 virtual DOM 반영 X)
  created() {
    console.log(process.env.NODE_ENV);
    // this.getMessage();
  },
};
</script>

<style>
.books-container button {
  color: #fafafa;
  border-radius: 10px;
}
</style>

module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:vue/essential",
    "prettier",
    "plugin:prettier/recommended",
    "@vue/prettier",
  ],
  plugins: ["prettier"],
  parserOptions: {
    parser: "@babel/eslint-parser",
    requireConfigFile: false,
    babelOptions: {
      babelrc: false,
      configFile: false,
    },
  },
};

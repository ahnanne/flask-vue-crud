module.exports = {
	root: true,
	env: {
		node: true,
	},
	extends: [
		'eslint:recommended',
		'plugin:vue/essential',
		'prettier',
		'plugin:prettier/recommended',
		'@vue/prettier',
	],
	plugins: ['prettier'],
	parserOptions: {
		parser: '@babel/eslint-parser',
		requireConfigFile: false,
		babelOptions: {
			babelrc: false,
			configFile: false,
		},
	},
	rules: {
		'prettier/prettier': [
			'error',
			{
				singleQuote: true,
				semi: true,
				useTabs: true,
				tabWidth: 2,
				trailingComma: 'all',
				printWidth: 80,
				bracketSpacing: true,
				arrowParens: 'avoid',
			},
		],
	},
};

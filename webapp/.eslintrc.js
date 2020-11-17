module.exports = {
  root: true,
  env: {
    node: true,
  },
  parserOptions:{
    'parser': 'babel-eslint',
    "ecmaVersion": 2017,
    parser: 'babel-eslint',
    sourceType: 'module',
    allowImportExportEverywhere: true
  },
  'extends': [
    'plugin:vue/strongly-recommended',
    /*"plugin:vue/vue3-strongly-recommended",*/
    "plugin:vue/recommended",
    "plugin:vue/essential"
  ],
  rules: {
    'indent': 'off',
    'vue/script-indent': ['warn', 2, {
    'baseIndent': 1
    }]
  },
  "overrides": [
    {
      "files": ["*.vue","*.js"],
      "rules": {
        "indent": "off"
      }
    }
  ]
};
/* eslint-disable */
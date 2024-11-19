// @ts-check
import tseslint from 'typescript-eslint';

export default tseslint.config(
  tseslint.configs.strictTypeCheckedOnly,
  {
    // this configuration is required for strictTypeCheckedOnly config to work
    languageOptions: {
      parserOptions: {
        // projectService: true,
        project: './tsconfig.json',
        tsconfigRootDir: import.meta.dirname,
      }
    },
  },
  {
    ignores: [
      'node_modules',
      'build',
      'dist',
      'eslint.config.mjs' // we ignore eslint.config.mjs because we don't want to type check this
    ]
  },
  {
    files: [
      "src/**/*.ts"
    ]
  },
);

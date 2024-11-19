# SETUP explained


## FOR TS-NODE

1. Initialize project
2. Install the following:
```
npm add --D typescript ts-node @types/node
```
3. Configure tsconfig
```
npx tsc --init
```



## WITH typescript-eslint

1. Do the steps above
2. Install dependencies
```
npm install --save-dev eslint @eslint/js typescript typescript-eslint
```
3. Create eslint.config.mjs and paste the following
```
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  eslint.configs.recommended,
  tseslint.configs.strictTypeCheckedOnly,
  {
    languageOptions: {
      parserOptions: {
        projectService: true,
        project: 'tsconfig.json',
        tsconfigRootDir: import.meta.dirname,
      }
    },
  },
  {
    ignores: ['node_modules', 'build', 'dist', "eslint.config.mjs"]
  },
  {
    files: [
      "src/**/*.ts"
    ]
  }
);
```

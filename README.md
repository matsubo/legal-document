# Legal document review

## Setup

```
% pip3 install openai
```

`OPENAI_API_KEY` をGitHub RepositoryのSecretsに設定

## Execution


Convert document from .docx to .md.
```
docker run --rm \
             --volume "$(pwd):/data" \
             --user $(id -u):$(id -g) pandoc/core jtuc/ikkai-keiyaku-jyuninin.docx -o jtuc/ikkai-keiyaku-jyuninin.md

```

Add annotation for heading.

```
OPENAI_API_KEY=sk-proj-xxxxx python3 convert.py jtuc/ikkai-keiyaku-jyuninin.md
```

Then create pull request by adding a new markdown format legal document.


#!/usr/bin/env bash
# Install screen-creative-skills into Claude Code / Cursor / Codex skill directories.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LANG_OPT="${2:-zh}" # zh | en
TARGET="${1:-}"

usage() {
  cat <<'EOF'
Usage:
  ./scripts/install-skills.sh <claude|cursor|codex|all> [zh|en]
  ./scripts/install-skills.sh <custom-dir> [zh|en]

Examples:
  ./scripts/install-skills.sh claude        # ~/.claude/skills (Chinese)
  ./scripts/install-skills.sh cursor en     # ~/.cursor/skills (English)
  ./scripts/install-skills.sh codex
  ./scripts/install-skills.sh all
  ./scripts/install-skills.sh .agents/skills zh   # project-local Codex path
EOF
}

if [[ -z "${TARGET}" ]]; then
  usage
  exit 1
fi

if [[ "${LANG_OPT}" == "en" ]]; then
  SRC="${ROOT}/english-version/category"
else
  SRC="${ROOT}/category"
fi

if [[ ! -d "${SRC}" ]]; then
  echo "Source not found: ${SRC}" >&2
  exit 1
fi

resolve_dirs() {
  case "$1" in
    claude) echo "${HOME}/.claude/skills" ;;
    cursor) echo "${HOME}/.cursor/skills" ;;
    codex)  echo "${HOME}/.agents/skills" ;;
    all)    echo "${HOME}/.claude/skills ${HOME}/.cursor/skills ${HOME}/.agents/skills" ;;
    *)      echo "$1" ;;
  esac
}

link_skills() {
  local dest="$1"
  mkdir -p "${dest}"
  local count=0
  # Flatten category/<type>/<skill-name> -> <dest>/<skill-name>
  while IFS= read -r -d '' skill_md; do
    local skill_dir
    skill_dir="$(dirname "${skill_md}")"
    local name
    name="$(basename "${skill_dir}")"
    local link_path="${dest}/${name}"
    if [[ -e "${link_path}" || -L "${link_path}" ]]; then
      rm -rf "${link_path}"
    fi
    ln -s "${skill_dir}" "${link_path}"
    count=$((count + 1))
  done < <(find "${SRC}" -mindepth 3 -maxdepth 3 -name SKILL.md -print0 | sort -z)
  echo "Installed ${count} skills -> ${dest}"
}

for dest in $(resolve_dirs "${TARGET}"); do
  link_skills "${dest}"
done

echo "Done. Invoke by name, e.g. /character-profile or ask the agent to use the skill."

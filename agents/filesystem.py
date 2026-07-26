from pathlib import Path

from deepagents.backends.composite import CompositeBackend
from deepagents.backends.filesystem import FilesystemBackend
from deepagents.backends.protocol import EditResult, FileUploadResponse, WriteResult

from backend.config import require

AGENTS_DIR = Path(__file__).parent
DENIED = "read-only: evidence is input and cannot be modified"


class ReadOnlyBackend(FilesystemBackend):
    def write(self, file_path, content):
        return WriteResult(error=DENIED, path=None)

    def edit(self, file_path, old_string, new_string, replace_all=False):
        return EditResult(error=DENIED, path=None, occurrences=None)

    def upload_files(self, files):
        return [FileUploadResponse(path=path, error=DENIED) for path, _ in files]


def create_backend():
    evidence = ReadOnlyBackend(root_dir=require("EVIDENCE_PATH"), virtual_mode=True)
    systems = FilesystemBackend(
        root_dir=str(Path(require("MODEL_REPO_PATH")) / "systems"), virtual_mode=True
    )
    return CompositeBackend(
        default=FilesystemBackend(root_dir=str(AGENTS_DIR), virtual_mode=True),
        routes={"/evidence/": evidence, "/systems/": systems},
    )

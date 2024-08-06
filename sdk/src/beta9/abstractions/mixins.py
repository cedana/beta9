from typing import Callable, Optional

from .. import terminal
from ..clients.gateway import DeployStubRequest, DeployStubResponse
from ..config import ConfigContext
from .base.runner import RunnerAbstraction


class DeployableMixin:
    func: Callable
    parent: RunnerAbstraction
    deployment_stub_type: str

    def _validate(self):
        if not hasattr(self, "func") or not isinstance(self.func, Callable):
            raise AttributeError("func variable not set or is incorrect type")

        if not hasattr(self, "parent") or not isinstance(self.parent, RunnerAbstraction):
            raise AttributeError("parent variable not set or is incorrect type")

        if not hasattr(self, "deployment_stub_type") or not self.deployment_stub_type:
            raise AttributeError("deployment_stub_type variable not set")

    def deploy(self, name: Optional[str] = None, context: Optional[ConfigContext] = None) -> bool:
        self._validate()

        name = name or self.parent.name
        if not name:
            terminal.error(
                "You must specify an app name (either in the decorator or via the --name argument)."
            )

        if context is not None:
            self.parent.config_context = context

        if not self.parent.prepare_runtime(
            func=self.func, stub_type=self.deployment_stub_type, force_create_stub=True
        ):
            return False

        terminal.header("Deploying")
        deploy_response: DeployStubResponse = self.parent.gateway_stub.deploy_stub(
            DeployStubRequest(stub_id=self.parent.stub_id, name=name)  # type: ignore
        )

        if deploy_response.ok:
            terminal.header("Deployed 🎉")
            self.parent.print_invocation_snippet(deploy_response.invoke_url)

        return deploy_response.ok

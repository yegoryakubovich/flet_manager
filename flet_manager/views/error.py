#
# (c) 2023, Yegor Yakubovich, yegoryakubovich.com, personal@yegoryakybovich.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from flet_core import Text, Row, IconButton, icons

from flet_manager.views.base import BaseView


class ErrorView(BaseView):
    route: str = '/error'
    app: None
    controls: list
    params: dict

    async def go_back(self, e):
        await self.app.view_change(go_back=True)

    async def build(self):
        self.controls = [
            Row(
                controls=[
                    IconButton(
                        icon=icons.ARROW_BACK,
                        icon_size=48,
                        tooltip='Go back',
                        on_click=self.go_back,
                    ),
                    Text(
                        value=self.params.get('error_code'),
                        size=48,
                    ),
                ],
            ),
        ]

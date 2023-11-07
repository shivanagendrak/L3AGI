from typing import Optional

from pydantic import UUID4, BaseModel


class ConfigInput(BaseModel):
    key: str
    value: str
    key_type: str
    is_secret: bool
    is_required: bool
    agent_id: Optional[UUID4]
    toolkit_id: Optional[UUID4]
    voice_id: Optional[UUID4]
    datasource_id: Optional[UUID4]
    workspace_id: Optional[UUID4]
    team_id: Optional[UUID4]
    session_id: Optional[str]


class ConfigOutput(BaseModel):
    id: str
    key: str
    value: str
    key_type: str
    is_secret: bool
    is_required: bool
    agent_id: Optional[UUID4]
    toolkit_id: Optional[UUID4]
    voice_id: Optional[UUID4]
    datasource_id: Optional[UUID4]
    team_id: Optional[UUID4]
    account_id: UUID4
    workspace_id: Optional[UUID4]
    is_deleted: bool
    created_by: Optional[UUID4]
    modified_by: Optional[UUID4]
    session_id: Optional[str]


class ConfigQueryParams(BaseModel):
    id: Optional[str]
    key: Optional[str]
    agent_id: Optional[UUID4]
    team_id: Optional[UUID4]
    toolkit_id: Optional[UUID4]
    datasource_id: Optional[UUID4]
    workspace_id: Optional[UUID4]
    session_id: Optional[str]


class AccountSettings(BaseModel):
    openai_api_key: Optional[str]
    hugging_face_access_token: Optional[str]
    replicate_api_token: Optional[str]
    pinecone_api_key: Optional[str]
    pinecone_environment: Optional[str]
    weaviate_url: Optional[str]
    weaviate_api_key: Optional[str]


class AccountVoiceSettings(BaseModel):
    deepgram_api_key: Optional[str]
    azure_speech_key: Optional[str]
    azure_speech_region: Optional[str]
    play_ht_api_key: Optional[str]
    play_ht_user_id: Optional[str]

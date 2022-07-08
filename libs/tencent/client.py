import json

from config import TENCENT_SECRET_ID, TENCENT_SECRET_KEY
from tencentcloud.common import credential
# from tencentcloud.common.profile.client_profile import ClientProfile
# from tencentcloud.common.profile.http_profile import HttpProfile
# from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import models, nlp_client


class TencentCloudClientInitError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"TencentCloudClient init Error{':' if self.message else ''} {self.message}."


class TencentCloudClient:
    def __init__(self, secret_id: str, secret_key: str):
        if not secret_id or not secret_key:
            raise TencentCloudClientInitError("secret_id 和 secret_key 不可为空")
        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
        # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
        cred = credential.Credential(secret_id, secret_key)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        # httpProfile = HttpProfile()
        # httpProfile.endpoint = "nlp.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        # clientProfile = ClientProfile()
        # clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        # client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)
        self.client = nlp_client.NlpClient(cred, "ap-guangzhou")
        # 实例化一个请求对象,每个接口都会对应一个request对象
        self.nlp_req = models.LexicalAnalysisRequest()

    def nlp_lexical_analysis(self, text: str) -> str:
        """
        raise TencentCloudSDKException
        """
        params = {"Text": text}
        self.nlp_req.from_json_string(json.dumps(params))
        # 返回的resp是一个LexicalAnalysisResponse的实例，与请求对象对应
        resp = self.client.LexicalAnalysis(self.nlp_req)

        # 输出json格式的字符串回包
        return resp.to_json_string()


client = TencentCloudClient(TENCENT_SECRET_ID, TENCENT_SECRET_KEY)

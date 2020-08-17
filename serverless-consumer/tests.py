import unittest
from handler import _byte_to_dict


class ConsumerCase(unittest.TestCase):
    def test_byte_to_dict(self):
        self.byte_value = b'{"headers": "{\\"Content-Type\\": \\"text/html\\", \\"Transfer-Encoding\\": \\"chunked\\", \\"Connection\\": \\"keep-alive\\", \\"Date\\": \\"Sun, 16 Aug 2020 11:16:06 GMT\\", \\"Last-Modified\\": \\"Sat, 15 Aug 2020 17:28:25 GMT\\", \\"ETag\\": \\"W/\\\\\\"e7e6a0e33f6b1e279c5cee58bc65b39a\\\\\\"\\", \\"Server\\": \\"AmazonS3\\", \\"Content-Encoding\\": \\"gzip\\", \\"Vary\\": \\"Accept-Encoding\\", \\"X-Cache\\": \\"Hit from cloudfront\\", \\"Via\\": \\"1.1 1360936ca0d2a8ac3134ac7c537d0e76.cloudfront.net (CloudFront)\\", \\"X-Amz-Cf-Pop\\": \\"HEL50-C1\\", \\"X-Amz-Cf-Id\\": \\"3A2mKDhhyc98QV8JowHqr19-Hp2xlPdChre5I88mEOvxYiF31Y4JWA==\\", \\"Age\\": \\"41953\\"}", "status_code": 200, "response_time": 0.07393193244934082}'
        self.message_value = self._byte_to_dict(byte_value)
        self.wanted_value = {'headers': '{"Content-Type": "text/html", "Transfer-Encoding": "chunked", "Connection": "keep-alive", "Date": "Sun, 16 Aug 2020 11:16:06 GMT", "Last-Modified": "Sat, 15 Aug 2020 17:28:25 GMT", "ETag": "W/\\"e7e6a0e33f6b1e279c5cee58bc65b39a\\"", "Server": "AmazonS3", "Content-Encoding": "gzip", "Vary": "Accept-Encoding", "X-Cache": "Hit from cloudfront", "Via": "1.1 1360936ca0d2a8ac3134ac7c537d0e76.cloudfront.net (CloudFront)", "X-Amz-Cf-Pop": "HEL50-C1", "X-Amz-Cf-Id": "3A2mKDhhyc98QV8JowHqr19-Hp2xlPdChre5I88mEOvxYiF31Y4JWA==", "Age": "41953"}', 'status_code': 200, 'response_time': 0.07393193244934082}
        self.asser_equal(message_value, wanted_value)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
#!/usr/bin/env python
import asyncio
import logging
from typing import Optional
import unittest
from os.path import join, realpath
import sys

from hummingbot.core.data_type.user_stream_tracker import UserStreamTrackerDataSourceType
from hummingbot.core.utils.async_utils import safe_ensure_future
from hummingbot.market.liquid.liquid_order_book_tracker import LiquidOrderBookTracker
from hummingbot.market.liquid.liquid_user_stream_tracker import LiquidUserStreamTracker

sys.path.insert(0, realpath(join(__file__, "../../../")))
logging.basicConfig(level=logging.DEBUG)


class LiquidOrderBookTrackerUnitTest(unittest.TestCase):
    order_book_tracker: Optional[LiquidOrderBookTracker] = None
    @classmethod
    def setUpClass(cls):
        cls.ev_loop: asyncio.BaseEventLoop = asyncio.get_event_loop()
        cls.user_stream_tracker: LiquidUserStreamTracker = LiquidUserStreamTracker(
            UserStreamTrackerDataSourceType.EXCHANGE_API)
        cls.user_stream_tracker_task: asyncio.Task = safe_ensure_future(cls.user_stream_tracker.start())

    def test_user_stream(self):
        # Wait process some msgs.
        self.ev_loop.run_until_complete(asyncio.sleep(120.0))
        print(self.user_stream_tracker.user_stream)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
import asyncio

from google.maps import solar_v1


async def main():
    client = solar_v1.SolarAsyncClient.from_service_account_file("credentials.json")

    request = solar_v1.FindClosestBuildingInsightsRequest()
    response = await client.find_closest_building_insights(request=request)

    print(response)


if __name__ == "__main__":
    asyncio.run(main())
